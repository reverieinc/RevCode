import codecs


def convert_revocode_sheet_to_map():

    fapth = "/Users/Rajat/Desktop/WORK/RnD/reflection-py/main/helpers/revcode/RevCode.tsv"
    with codecs.open(fapth, "r", "utf-8") as fin:
        for line in fin:
                line_t = line.split("\t")

                # local_to_rev
                # print line_t[21]+ " : \""+line_t[0]+"\""+ ", #  "+line_t[22]

                # rev_to_local
                print "\""+line_t[0]+"\" : "+line_t[21] + ", #  "+line_t[22]

if __name__ == '__main__':

    convert_revocode_sheet_to_map()

