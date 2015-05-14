from ctree import Tree

class Parser(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def compile(self):

        if (self._gen_tree()):
            self._process_tree()

    def _gen_tree(self):
        s = self.scanner

        if (s.next() != 'BEGIN'):
            print("Error: the program must begin with keyword BEGIN. line: %d" % s.line)
            return False

        self.tree = Tree('ROOT')
        self.current_node = self.tree.root

        status = "C" #C-Continue, E-Error

        while status == "C":

            term = s.next()

            if (term == None):
                break

            if (self.current_node == None):
                print("Error: unexpected term %s. the program already has been end. line: %d" % (term, s.line))
                return False

            if (term == 'OP'):
                status = self._op()

            elif (term == 'LOOP'):
                status = self._loop()

            elif (term == 'END'):
                status = self._end()

            else:
                print("Error: unexpected term %s. line: %d" % (term, s.line))
                status = "E"

        if (status == "E"):
            return False

        if (self.current_node):
            print("Error: unexpected end. line: %d" % (s.line))
            return False

        return True

    def _process_tree(self):
        self.tree.preorder()

    def _op(self):
        s = self.scanner
        number = s.next()

        try:
            number = int(number)
        except ValueError:
            print("Error: unexpected term %s, expected number. line: %d" % (number, s.line))
            return "E"

        self.current_node.add_child("OP %d" % number)
        print("new OP", self.current_node.value)

        return "C"

    def _loop(self):

        s = self.scanner
        number = s.next()

        if (number != "n"):
            try:
                number = int(number)
            except ValueError:
                print("Error: unexpected term %s, expected number or n. line: %d" % (number, s.line))
                return "E"

        self.current_node = self.current_node.add_child("LOOP %s" % number)
        print('new node', self.current_node.value);

        return "C" 

    def _end(self):

        self.current_node = self.current_node.parent
        print('return to last node', (self.current_node and self.current_node.value) or 'END')

        return "C"
