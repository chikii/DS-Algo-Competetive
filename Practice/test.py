import time

class Transportation_Problem:

    def __init__(self, supply, demand):

        self.supply = supply
        self.demand = demand
        self.limit = supply+demand-1
        self.matrix = []

        self.show_dummy_table()

        while True:
            self.take_values(supply, demand)
            self.show_table(self.matrix)
            is_satisfy = input('Is Table Correct (y/n): ')
            if is_satisfy == 'y' or is_satisfy == 'Y' or is_satisfy == 'yes' or is_satisfy == 'yes' or is_satisfy == 'Yes': break
            else:
                print()
                print('Enter Values Again.')
        
        self.solve()

    def show_dummy_table(self):
        print()
        print('This is the dummy Table -> ')
        supply, demand = 3, 3

        print('\t',end = '')
        for d in range(demand):
            print(f'D{d+1}', end='\t')
        print('Supply')

        x = 1
        for i in range(supply):
            print(f'S{i+1}',end= '\t')
            for j in range(demand):
                print(f'x{x}',end = '\t')
                x +=1
            print('  s')

        print('Demand', end= '\t')
        for d in range(demand):
            print('d', end = '\t')
        
        print()
    
    def take_values(self, supply, demand):
        matrix = []
        print()
        print('Enter Each Row Values Seperated by Space.')
        print('NOTE - Last value should be supply Value for that particular row.')
        for i in range(supply):
            while True:
                row = list(map(int, input(f'Enter Values for Row - {i+1} : ').split()))
                if len(row) == demand+1:
                    matrix.append(row)
                    break
                else:
                    print('Invalid Input!!!')

        
        while True:
            demands = list(map(int, input('Enter Demand Values, Seprated by Space : ').split()))
            if len(demands) == demand:
                matrix.append(demands)
                break
            else:
                print('Invalid Input!!!')
            
        self.matrix = matrix

    def show_table(self, matrix):
        # matrix = self.matrix
        demand = len(matrix[-1]) # self.demand
        supply = len(matrix)-1 # self.supply
        
        print('\t',end = '')
        for d in range(demand):
            print(f'D{d+1}', end='\t')
        print('Supply')

        for i in range(supply):
            print(f'S{i+1}',end= '\t')
            for j in range(demand):
                print(f'{matrix[i][j]}',end = '\t')
            print(matrix[i][-1])

        print('Demand ', end= ' ')
        for d in range(demand):
            print(matrix[-1][d], end = '\t')
        
        print()


    def solve(self):

        print('\n\n')
        print('<------------------------ SOLUTION ------------------------> ')
        
        matrix = self.matrix
        limit = self.limit

        supply = self.supply
        demand = self.demand
        total_supply, total_demand = 0, 0

        total_demand = sum(matrix[-1])
        total_supply = sum(matrix[i][-1] for i in range(supply))
        diff = abs(total_demand-total_supply)

        print('Total Demand : ', total_demand)
        print('Total Suppy  : ', total_supply)

        # when supply is greater,
        if total_supply > total_demand:
            print('Total Supply is greater than total Demand.')
            print('So, Adding Extra column with 0 values.')
            for i in range(supply):
                matrix[i].insert(-1, 0)
            matrix[-1].append(diff)
            
            print('New table is -> ')
            self.show_table(matrix)

        # when demand is greater
        elif total_supply < total_demand:
            print('Total Demand is greater than total Supply.')
            print('So, Adding Extra row with 0 values.')
            new_row = [0 for i in range(demand)]
            new_row.append(diff)
            matrix.insert(-1, new_row)

            print('New table is -> ')
            self.show_table(matrix)
        # when both are equal
        else:
            print('Total Demand is equal to total Supply. We can proceed.')
            # show_table(matrix)
        print()


        ans = 0
        dp_ans = []
        curr_cell = (0,0)

        print()
        while True:
            time.sleep(3)
            print('-------------------------------------------------------')
            i,j = curr_cell
            if i >= len(matrix) or j >= len(matrix[-1]): break

            curr_supply = matrix[i][-1]
            curr_demand = matrix[-1][j]
            diff = abs(curr_demand-curr_supply)
            
            if curr_supply > curr_demand:
                dp_ans.append((curr_demand, curr_cell))
                print(f'Taking S{i+1}D{j+1}')
                print(f'Current Supply : {curr_supply}, Current Demand : {curr_demand}')
                print('Current Supply is Greater than Current Demand : ')

                ans += matrix[i][j] * matrix[-1][j]

                matrix[i][-1] -= matrix[-1][j]
                matrix[-1][j] = 0

                print('Now table is -> ')
                self.show_table(matrix)
                curr_cell = i, j+1

                print(f'Total Cost : {ans}')
                print()

            elif curr_demand > curr_supply:
                dp_ans.append((curr_supply, curr_cell))
                print(f'Taking S{i+1}D{j+1}')
                print(f'Current Supply : {curr_supply}, Current Demand : {curr_demand}')
                print('Current Demand is Greater than Current Supply : ')

                ans += matrix[i][j] * matrix[i][-1]

                matrix[-1][j] -= matrix[i][-1]
                matrix[i][-1] = 0

                print('Now table is -> ')
                self.show_table(matrix)
                curr_cell = i+1, j

                print(f'Total Cost : {ans}')
                print()
            else:
                dp_ans.append((curr_supply, curr_cell))
                print(f'Taking S{i+1}D{j+1}')
                print(f'Current Supply : {curr_supply}, Current Demand : {curr_demand}')
                print('Current Demand is equal to Current Supply : ')
                
                ans += matrix[i][j] * matrix[i][-1]
                
                matrix[i][-1] = 0
                matrix[-1][j] = 0
                print('Now table is -> ')
                self.show_table(matrix)
                curr_cell = i+1, j+1
                print(f'Total Cost : {ans}')
                print()

        print('Minimum Total Transportation Cost : ', end = '')

        for i in range(len(dp_ans)):
            cell_val = matrix[dp_ans[i][1][0]][dp_ans[i][1][1]]
            cost =  dp_ans[i][0]
            print(f'({cost} X {cell_val}) + ' , end = '' )

        print(f' = {ans}')

        cell_allocated = len(dp_ans)
        print(f'Here, Number of allocated cell : {cell_allocated}', end = ' ')

        if cell_allocated < limit:
            print(f'which is less than (m+n-1){limit}.')    
            print('Therefore, The solution is Degenerate.')
        else:
            print(f'which is Greater/Equal than (m+n-1){limit}.')    
            print('Therefore, The solution is Non-Degenerate.')


def main():

    while True:
            
        supply = int(input('Enter Supply Constrains : '))
        demand = int(input('Enter Demand Constrains : '))
        Transportation_Problem(supply, demand)

        continue_ = input('\n\nDo You want to solve another question?(y/n)')
        if continue_ != 'y':
            print('Thank  You !!! :)')
            break

try:
    main()
except Exception as e:
    print('Opps Something Wrong Happened...! Please Try Again.')
    print('Exception :',e)