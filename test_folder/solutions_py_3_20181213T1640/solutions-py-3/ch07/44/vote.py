import statistics
import scipy.stats

#3 lists for each machine to hold data on all 3 ratios
#optical
opt_ng=[]
opt_bb=[]
opt_ou=[]
#votomatic
vot_ng=[]
vot_bb=[]
vot_ou=[]
#datavote
data_ng=[]
data_bb=[]
data_ou=[]
#skip hand and lever for small size


infile = open("fl2000.txt")
#skip header
infile.readline()
for line in infile :
    data=line.split()
    under=int(data[3])
    over=int(data[4])
    bush=int(data[5])
    gore=int(data[6])
    nader=int(data[8])
    buch=int(data[11])
    if data[1]=='"Optical"':
        opt_ng.append(nader/gore)
        opt_bb.append(buch/bush)
        opt_ou.append(over/under)
    elif data[1]=='"Votomatic"':
        vot_ng.append(nader/gore)
        vot_bb.append(buch/bush)
        vot_ou.append(over/under)
    elif data[1]=='"Datavote"':
        data_ng.append(nader/gore)
        data_bb.append(buch/bush)
        data_ou.append(over/under)


#anova analysis
p = scipy.stats.f_oneway(opt_ng, vot_ng, data_ng)[1]
print("p value for nader/gore: %f" % p)

p = scipy.stats.f_oneway(opt_bb, vot_bb, data_bb)[1]
print("p value for bush/buchanan: %f" % p)

p = scipy.stats.f_oneway(opt_ou, vot_ou, data_ou)[1]
print("p value for over/under: %f" % p)
        

