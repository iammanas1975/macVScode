import graphviz
dot = graphviz.Digraph('round-table', comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
dot.render('round-table.gv').replace('\\', '/')
dot.render('round-table.gv', view=True).replace('\\', '/')