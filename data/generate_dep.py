import json

def write_sym(lista):
	values = []
	operators = []
	priority = {'+': 0, '-': 0, '*': 1, '/': 1}

	sym_dict = ["" for i in range (50)]
	exp_dict = ["" for i in range (50)]

	for (i,sym) in enumerate(lista):
		sym_dict[i+1] = sym

		if sym.isdigit():
			values.append(i+1)
		elif sym == "!":
			val_id = values.pop()
			val_string = "{} {} _ _ NUM _ {} num _ _\n".format(val_id, sym_dict[val_id], i+1)
			exp_dict[val_id] = val_string
			values.append(i+1)
		else:
			while len(operators) > 0 and priority[sym_dict[operators[-1]]] >= priority[sym]:
				op = operators.pop()
				right = values.pop()
				left = values.pop()

				if (sym_dict[right].isdigit()):
					right_string = "{} {} _ _ NUM _ {} num _ _\n".format(right, sym_dict[right], op)
					exp_dict[right] = right_string
				elif (sym_dict[right] == "!"):
					right_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(right, sym_dict[right], op)
					exp_dict[right] = right_string
				else:
					right_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(right, sym_dict[right], op)
					exp_dict[right] = right_string

				if (sym_dict[left].isdigit()):
					left_string = "{} {} _ _ NUM _ {} num _ _\n".format(left, sym_dict[left], op)
					exp_dict[left] = left_string
				elif (sym_dict[left] == "!"):
					left_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(left, sym_dict[left], op)
					exp_dict[left] = left_string
				else:
					left_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(left, sym_dict[left],  op)
					exp_dict[left] = left_string

				values.append(op)

			operators.append(i+1)

	while len(operators) > 0:
		op = operators.pop()
		right = values.pop()
		left = values.pop()

		if (sym_dict[right].isdigit()):
			right_string = "{} {} _ _ NUM _ {} num _ _\n".format(right, sym_dict[right], op)
			exp_dict[right] = right_string
		elif (sym_dict[right] == "!"):
			right_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(right, sym_dict[right], op)
			exp_dict[right] = right_string
		else:
			right_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(right, sym_dict[right], op)
			exp_dict[right] = right_string

		if (sym_dict[left].isdigit()):
			left_string = "{} {} _ _ NUM _ {} num _ _\n".format(left, sym_dict[left], op)
			exp_dict[left] = left_string
		elif (sym_dict[left] == "!"):
			left_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(left, sym_dict[left], op)
			exp_dict[left] = left_string
		else:
			left_string = "{} {} _ _ CCONJ _ {} dep _ _\n".format(left, sym_dict[left], op)
			exp_dict[left] = left_string

		values.append(op)

	root_op = values.pop()
	root_string = "{} {} _ _ CCONJ _ 0 root _ _\n".format(root_op, sym_dict[root_op])
	exp_dict[root_op] = root_string

	# return exp_dict
	with open ("expr_test.conll", "a") as f1:
		for sym in exp_dict:
			if len(sym):
				f1.write(sym)
		f1.write("\n")

with open ("expr_test.json", "r") as f:
	all_data = json.load(f)
	for data in all_data:
		write_sym(data["expr"])
# print (write_sym(['6', '+', '6', '+', '2', '+', '9']))