
import numpy as np

class Mesh:

    def __init__(self):
        self.nV = 0 
        self.nF = 0
        self.vertexBuffer = None
        self.idxBuffer = None

    def loadMesh(self, filename):

        with open(filename, 'rt') as inputFile:            
            # 정점의 개수를 읽는다.
            self.nV = int(next(inputFile))
            # 정점을 담을 버텍스 배열을 준비한다.
            self.vertexBuffer = np.zeros(shape = ( self.nV * 3, ), dtype = float)
            # self.nV 정점의 개수만큼 반복적으로 정점 정보를 읽는다.
            for i in range(self.nV):
                input_string = next(inputFile)
                start = i * 3
                end = start + 3
                self.vertexBuffer[start: end] = input_string.split()
            # 면의 개수를 읽어 보자
            self.nF = int(next(inputFile))
            # 면을 구성하는 인덱스의 배열을 준비한다.
            self.idxBuffer = np.zeros( shape = ( self.nF * 3), dtype = int)
            # self.nF 면의 개수만큼 세 개의 색인(index)를 읽어들인다.
            for i in range(self.nF):
                input_string = next(inputFile)
                start = i * 3
                end = start + 3
                self.idxBuffer[start: end] = input_string.split()[1:4]


                


    def print_info(self):
        print(f'정점의 개수는 {self.nV}개')
        print(f'면의 개수는 {self.nF}개')
        print(f'정점 배열 {self.vertexBuffer}')
        print(f'색인 배열 {self.idxBuffer}')


myMesh = Mesh()
myMesh.loadMesh('./Code05/myMesh.txt')

myMesh.print_info()

