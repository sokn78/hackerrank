def checkBST(root):
    def checkBST(node, minCondition, maxCondition):
        if (node.data <= minCondition) | (node.data >= maxCondition):
            return False
        if node.left == None:
            left_condition = True
        else:
            left_condition = checkBST(node.left, minCondition, node.data)
        if node.right == None:
            right_condition = True
        else:
            right_condition = checkBST(node.right, node.data, maxCondition)
        return left_condition & right_condition

    return checkBST(root, float('-inf'), float('+inf'))