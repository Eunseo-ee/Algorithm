def solution(array, commands):
    answer = []
    
    for x in commands:
        [i,j,k] = x
        new_array=array[:]
        new_array=new_array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
    
    return answer