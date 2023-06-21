import sys

class QuickMetaPlugin:
    def input(self, inputfile):
        self.groupcounts = dict()
        infile = open(inputfile, 'r')
        for line in infile:
            contents = line.strip().split('\t')
            self.groupcounts[contents[0]] = int(contents[1])

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        for key in self.groupcounts:
            for i in range(self.groupcounts[key]):
                outfile.write(key+"\t")
        outfile.write("\n")
