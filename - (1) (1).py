#open and read all text files
one = open("Seq1.txt", 'r')
seq1 = one.read()
two = open("Seq2.txt", 'r')
seq2 = two.read()
three = open("Seq3.txt", 'r')
seq3 = three.read()
four = open("Seq4.txt", 'r')
seq4 = four.read()
five = open("Seq5.txt", 'r')
seq5 = five.read()
six = open("Seq7.txt", 'r')
seq6 = six.read()
seven = open("Seq8.txt", 'r')
seq7 = seven.read()
eight = open("Seq9.txt", 'r')
seq8 = eight.read()
nine = open("Seq10.txt", 'r')
seq9 = nine.read()
ten = open("Seq11.txt", 'r')
seq10 = ten.read()
ele = open("Seq12.txt", 'r')
seq11 = ele.read()
twelve = open("Seq13.txt", 'r')
seq12 = twelve.read()
tt = open("Seq14.txt", 'r')
seq13 = tt.read()
fourt = open("Seq15.txt", 'r')
seq14 = fourt.read()
fift = open("Seq16.txt", 'r')
seq15 = fift.read()
sixt = open("Seq17.txt", 'r')
seq16 = sixt.read()
sevent = open("Seq18.txt", 'r')
seq17 = sevent.read()
eightt = open("Seq19.txt", 'r')
seq18 = eightt.read()




#defines the function to find Gs and Cs in a DNA sequence
def percentgc(seq):
    #makes a counter to find total number of characters in the text file (needed for G/C %)
    c = -1
    #makes a counter to count number of Gs and Cs in DNA sequence
    gc = 0
    #creates a for loop to find number of Gs and Cs in DNA sequence
    for char in seq:
        #increases counter by 1 for each character in the sequence
        c+=1
        #increases gc counter by 1 when there is a G or C in the sequence
        if char == "G" or char=="C":
            gc += 1
        #continues the for loop if the character in the sequence is an A or T
        else: 
            continue
    #calculates the percentage of Gs and Cs in the whole sequence
    gcpercent = ((gc)/ c) * 100
    print("% G/C:", gcpercent)
    #matches the sequence to the correct type of bacteria based 
    #on the amount of Gs and Cs in the sequence
    if 22 <= gcpercent < 45:
        bactype = "Bateriodetes"
    if 45 <= gcpercent < 50:
        bactype = "Proteobacteria"
    if 50 <= gcpercent <= 60:
        bactype = "Acidobacteria"
    if 65 <= gcpercent <= 80:
        bactype = "Actinobacteria"
    print("Type of Bacteria:", bactype)
 
#use tbe function for all of the sequences to find the percentage of G/C and the type of bacteria
percentgc(seq1)
percentgc(seq2)
percentgc(seq3)
percentgc(seq4)
percentgc(seq5)
percentgc(seq6)
percentgc(seq7)
percentgc(seq8)
percentgc(seq9)
percentgc(seq10)
percentgc(seq11)
percentgc(seq12)
percentgc(seq13)
percentgc(seq14)
percentgc(seq15)
percentgc(seq16)
percentgc(seq17)
percentgc(seq18)