'''
Created on 2017年1月19日

@author: 薛沛雷
'''


class HMM:
    
    #HMM五元组(S,K,A,B,Pi)初始化
    def __init__(self,S,K,A,B,Pi,O):
        self.S=S
        self.K=K
        self.A=A
        self.B=B
        self.Pi=Pi
        self.O=O
       
    #前向算法：1.初始化，2：归纳计算，3：求和终结
    def forwardProcedure(self):
        #初始化
        sums=0.0
        num=0
        p=0
        count=1
        #申请相应的二元数组
        alpha=[[0 for col in range(0,len(S))] for row in range(0,len(O))]
        for keys in Pi.keys():
            alpha[0][num]=Pi[keys]*B[keys][O[0]]
            num+=1
            
        #归纳计算
        for times in range(len(O)-1):
            #当前的行
            rowNum=int(num/len(S))
            #当前的列
            colNum=num%len(S)
            for j in S:
                for i in A.keys():
                    #累加的前半部分
                    sums+=alpha[rowNum-1][colNum]*A[i][j]
                #根据前面所有节点计算出下一个节点，并存入二维数组
                alpha[rowNum][colNum]=sums*B[j][O[count]]
                colNum+=1
                num+=1
            count+=1
                
        #求和终结
        for final in range(len(S)):
            p+=alpha[len(O)-1][final]
        return p
    
    
    
            
    
    #维特比算法：1.初始化，2.归纳计算，3.终结，4.路径回溯
    def viterbi(self):
        
        #申请维特比变量delta和记录路径的变量path
        delta=[0]*len(S)
        paths=[]
        num=0
        count=1
        
        #初始化
        for i in Pi.keys():
            delta[num]=Pi[i]*B[i][O[0]]
            num=(num+1)%len(S)
        paths.append(S[delta.index(max(delta))])
        
        #归纳计算
        for i in range(len(O)-1):
            maxium=max(delta)
            position=delta.index(maxium) 
            for j in S:
                delta[num]=maxium*A[S[position]][j]*B[j][O[count]]
                num=(num+1)%len(S)
            count+=1
            #记录路径
            paths.append(S[position])
        return paths
           
        
        
            
if __name__ == "__main__":

    #S为状态的集合
    S=("高兴","不高兴")
    #K为输出符号的集合
    K=("你好坏呀","你有毛病吧","你猜")
    #pi为初始状态的概率分布
    Pi={"高兴":0.7,"不高兴":0.3}
    #A为状态转移概率
    A={
       "高兴":{"高兴":0.4,"不高兴":0.6},
       "不高兴":{"高兴":0.2,"不高兴":0.8}
       }
    #B为符号发射概率
    B={
       "高兴":{"你好坏呀":0.6,"你有毛病吧":0.3,"你猜":0.1},
       "不高兴":{"你好坏呀":0.1,"你有毛病吧":0.7,"你猜":0.2}
       }
    #O为观察序列
    O=[K[1],K[0],K[2],K[1],K[1],K[2]]
    
    hmm=HMM(S,K,A,B,Pi,O)
    print(hmm.forwardProcedure())
    print(hmm.viterbi())
    
    
    
    
    
    