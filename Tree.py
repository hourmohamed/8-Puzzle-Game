class Tree:
    def move(self, currState, offset):
        zIdx = currState.index("0")
        nIdx = zIdx + int(offset)
        currState_list = list(currState)
        if 0 <= nIdx < len(currState):
            currState_list[zIdx], currState_list[nIdx] = currState_list[nIdx], currState_list[zIdx]
            newState = ''.join(currState_list)
        return newState
            
    def valid_move(self, current_state):
        new_states = ""

        zero_index = current_state.index("0")

        
        if zero_index % 3 < 2:
            # moves to the right
            new_states= new_states + "".join("1,")
        
        if zero_index // 3 > 0:
            # move up
             new_states= new_states + "".join("-3,")
        if zero_index // 3 < 2:
            # move down
             new_states= new_states + "".join("3,")
        if zero_index % 3 > 0:
            # moves to the left
            new_states= new_states + "".join("-1,")
      

        return new_states


# if __name__ =="__main__":

#     tree = Tree()


