from collections import defaultdict

class IBM_ModelOne(object):
    def __init__(self, source, target, iterations):
        self.iterations = iterations
        
        self.slines = []
        self.tlines = []

        self.src_dict = {}
        self.tgt_dict = {}
        self.src_tgt_dict = {}

        with open(source) as src, open(target) as tgt:
            self.slines = src.readlines()
            self.tlines = tgt.readlines()

        for i in range(len(self.slines)):
            s_words = self.slines[i].strip().split()
            t_words = self.tlines[i].strip().split()
            for s_word in s_words:
                self.src_dict[s_word] = 1
                for t_word in t_words:
                    self.tgt_dict[t_word] = 1
                    self.src_tgt_dict[(t_word, s_word)] = 0
    
    def initialize(self):
        src_vocab_size = len(self.src_dict)
        for (tgt, src) in self.src_tgt_dict:
            self.src_tgt_dict[(tgt, src)] = 1.0 / src_vocab_size
    
    def em_round(self):
        count = defaultdict(float)
        total = defaultdict(float)
        
        for i in range(len(self.slines)):
            s_words = self.slines[i].strip().split()
            t_words = self.tlines[i].strip().split()
            s_total = defaultdict(float)
            for t_word in t_words:
                for s_word in s_words:
                    s_total[t_word] += self.src_tgt_dict[(t_word, s_word)]
            for t_word in t_words:
                for s_word in s_words:
                    count[(t_word, s_word)] += self.src_tgt_dict[(t_word, s_word)] / s_total[t_word]
                    total[s_word] += self.src_tgt_dict[(t_word, s_word)] / s_total[t_word]
        
        for s_word in self.src_dict:
            for t_word in self.tgt_dict:
                self.src_tgt_dict[(t_word, s_word)] = count[(t_word, s_word)] / total[s_word]
        
    def train(self):
        self.initialize()
        for i in range(self.iterations):
            self.em_round()

def main():
    source_file = "src.txt"
    target_file = "tgt.txt"
    iterations = 20

    model = IBM_ModelOne(source_file, target_file, iterations)
    model.train()

    with open("out.txt", 'w') as fout:
        for (src_word, tgt_word) in model.src_tgt_dict:
            if not model.src_tgt_dict[(src_word, tgt_word)] == 0.0 or not model.src_tgt_dict[(src_word, tgt_word)] == 1.0:
                fout.write(src_word + " " + tgt_word + " " + str(model.src_tgt_dict[(src_word, tgt_word)]) + "\n")

if __name__ == "__main__":
    main()