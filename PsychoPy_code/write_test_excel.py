import random
import xlsxwriter
data_colums = ['withoutP1', 'correct_key1'];
class WriteExcel:
    def __init__(self, pathNamPrefix, excelFileName, colums1_name, colums2_name, loopNum=30, total_file_num=150):
        self.pathNamPrefix = pathNamPrefix
        self.loopNum = loopNum
        self.excelFileName = excelFileName
        self.total_file_num = total_file_num
        self.colums1_name = colums1_name
        self.colums2_name = colums2_name

    def write(self):
        # Generate a random list with self.loopNum elements
        randomList = random.sample(range(1, self.total_file_num), self.loopNum)
        # Generate a list with pathNamePrefix + randomList[i] + .png
        pathNameList_left = [self.pathNamPrefix + '_left_' + str(i) + '.png' for i in randomList]
        randomList = random.sample(range(1, self.total_file_num), self.loopNum)
        pathNameList_right = [self.pathNamPrefix + '_right_' + str(i) + '.png' for i in randomList]
        # Generate a list with element 's' and data numner if self.loopNum
        correct_key_left = ['s'] * self.loopNum
        correct_key_right = ['k'] * self.loopNum
        # Merge pathNameList_left and pathNameList_right
        pathNameList = pathNameList_left + pathNameList_right
        # Merge correct_key_left and correct_key_right
        correct_key = correct_key_left + correct_key_right

        # create a new lists with pathNameList and correct_key
        pathNameList_2wr = []
        for i in range(len(pathNameList)):
            pathNameList_2wr.append([pathNameList[i], correct_key[i]])

        workbook = xlsxwriter.Workbook(self.excelFileName)
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, self.colums1_name)
        worksheet.write(0, 1, self.colums2_name)
        row = 1
        col = 0
        for pathName, correct_key in (pathNameList_2wr):
            worksheet.write(row, col, pathName)
            worksheet.write(row, col + 1, correct_key)
            row += 1

        workbook.close()

