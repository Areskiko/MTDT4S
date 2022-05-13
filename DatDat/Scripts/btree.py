from dis import pretty_flags

def print_tree(root, level1, leafs):
  print("_"*54)
  print("\t\t\t"+pretty([root]))
  if level1 != []:
    print("\t"+(pretty(level1)))
  if leafs!= []:
    print(pretty(leafs))


def pretty(lists):
    sum=""
    for list in lists:
      out= "["
      for i in list:
        out+=str(i)+", "
      out=out[:-2]
      out += "]\t\t"
      sum += out
    return sum

def main():
    
  size =3 #int(input("Skriv inn 3 eller 4 for blokkstørrelse"))
  seq = input("Skriv en sekvens av poster separert med mellomrom> ")
  steps = input("Skriv y for å vise steg> ")
  is_steps = steps == "y"
  seqList =[int(post) for post in seq.split()]

  if(size == 3):
    heigth = 1
    root=[]
    level1=[]
    leafs = []
    
    while seqList:
      if(steps):
        print_tree(root, level1, leafs)
        input()
      post = seqList.pop(0)   

      if(heigth==1):
        if len(root)==3:
          leafs = [root[:2], root[2:]]
          root = root[2:]
          heigth += 1
          seqList.insert(0, post)
        else:
          root.append(post)
          root.sort()
      elif(heigth==2):
        i=0
        for r_post in root:
          if post < r_post:
            break
          else:
            i+=1

        j=0
        for l_post in leafs[i]:
          if post < l_post:
            break
          else:
            j+=1

        if len(leafs[i])==3: #needs split
          split_post= leafs[i].pop()
          leafs.insert(i+1, [split_post])
          
          if len(root)==3: #root is full
            heigth+=1
            level1=[[root[0]], [root[2]]]
            root=[root[1]]
            if i<2:
              level1[0].insert(i, split_post)
            else:
              level1[1].insert(i-2, split_post)
          else:
            root.insert(i, split_post)

          if(j==3):
            leafs[i+1].append(post)
          else:
            leafs[i].insert(j, post)
            
        else: #no split needed, insert at right pos
          leafs[i].insert(j, post)
      elif(heigth==3):
        i=0
        for r_post in root:
          if post < r_post:
            break
          else:
            i+=1

        k=0
        for i_post in level1[i]:
          if post < i_post:
            break
          else:
            k+=1
        leaf_i=k
        for x in range(i):
          leaf_i+=len(level1[x])+1

        j=0
        for l_post in leafs[leaf_i]:
          if post < l_post:
            break
          else:
            j+=1


        if len(leafs[leaf_i])==3: # leaf needs split
          split_post= leafs[leaf_i].pop()
          leafs.insert(leaf_i+1, [split_post])
          
          if len(level1[i])==3: #inner node is full
            inner_split_post= level1[i][1]
            level1.insert(i+1, [level1[i][2]])
            level1[i]=[level1[i][0]]
            
            root.insert(i, inner_split_post)
            if k<2:
              level1[i].insert(k, split_post)
            else:
              level1[i+1].insert(k-2, split_post)
          else:
            level1[i].insert(k, split_post)

          if(j==3):
            leafs[leaf_i+1].append(post)
          else:
            leafs[leaf_i].insert(j, post)
            
        else: #no split needed, insert at right pos
          leafs[leaf_i].insert(j, post)

 
    print_tree(root, level1, leafs)

main()
input()
