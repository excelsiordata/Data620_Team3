from graphviz import Digraph
dot = Digraph(comment='C suite')
dot
dot.node('A', 'CEO')
dot.node('B', 'CFO')
dot.node('C', 'COO')
dot.node('D', 'CIO')
dot.node('E', 'CDO')
dot.node('F', 'CAO')
dot.edges(['AB','AC','BD','CE','BF'])
dot.edge('D','F',constraint='false')
print(dot.source)
dot.render('test-output/c-suite.gv', view=True)
'test-output/c-suite.gv.pdf'

