#Eddie Neitenbach
#Lab Section: 11
#Submission date: 11/12/2024



def file(in_file, out_file):
    with open(in_file) as input_file, open(out_file) as output_file:
        for create in input_file:
            create = create.strip()
            couple = create.split("\t")
            produced = ""
            for couple in couples:
                key, value = couple.split(":")
                count = int(value)
                if key == "w":
                    poroduced += " " * count 
                elif key == "*":
                    produced += "*" * count
            print(produced)
            output_file.write(produced + "\n")

