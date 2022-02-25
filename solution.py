class Task():
    def __init__(self,NoContr,NoProj):
        self.NoContributers = int(NoContr)
        self.Noprojects = int(NoProj)
        self.contributers = {} #2d
        self.projects = {}
        
    def ProjectsAndContributers(self,ip_file):
        with open(ip_file) as f :
            d = f.readline()
            for i in range(1,self.NoContributers + 1):
                data = f.readline().strip('\n').split(' ')
                Name, NoSkill = data[0], data[1]
                self.contributers[Name] = NoSkill
                skill = {}
                for j in range(int(NoSkill)):
                    s = f.readline().strip('\n').split(' ')
                    skill[s[0]] = int(s[1])
                    
                self.contributers[Name] = skill

            for i in range(1,self.Noprojects + 1):
                data = f.readline().strip('\n').split(' ')
                PjtName, NoDays, NoRoles = data[0], data[1], data[4]
                self.projects[PjtName] = NoRoles
                roles = {}
                for j in range(int(NoRoles)):
                    s = f.readline().strip('\n').split(' ')
                    roles[s[0]] = int(s[1])
                    
                self.projects[PjtName] = roles
                
            print(self.projects)
            print(self.contributers)

    def Assign(self,op_file):
        assign = [str(self.Noprojects)]        
        Pending = self.Noprojects
    
        for k in self.projects:
            p = list(self.projects[k].keys())
            q = list(self.projects[k].values())
            for j in self.contributers:
                c = list(self.contributers[j].keys())
                b = list(self.contributers[j].values())
                for r in p:
                    for d in c:            
                        if r == d :#and self.projects[k][r] <= self.contributers[j][d] :
                            if '\n'+ k +'\n' not in assign:
                                Pending -= 1
                                assign.append('\n'+ k +'\n')                            
                            assign.append(j + ' ')
                            self.contributers[j][d] += 1
        # assign.append('\n')
        print(assign)
        
        with open(op_file,'w') as op:
            op.writelines(assign)
            
                                            

filename = 'a_an_example.in'
ip_file = 'input\\' + filename + '.txt'
op_file = 'output\\' + filename + '.op.txt'

file = open(ip_file,'r')
ContrbProj = file.readline().strip('\n').split(' ')
NoContributers = ContrbProj[0]
NoProjects = ContrbProj[1]
file.close()

T = Task(NoContributers, NoProjects)
T.ProjectsAndContributers(ip_file)
T.Assign(op_file)
