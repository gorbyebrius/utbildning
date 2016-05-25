# -*- coding: UTF-8 -*-
import re


# Create a string with the logic
# only_acceptable_form => ( φ ) → ( ψ )
# sentence = "( P → Q ) → ( ¬ Q → ¬ P )"
# sentence = "( P ∨ R ) → ( P ∨ Q )"
# sentence = "( P ∨ R ) ∧ ( P ∨ Q )"
sentence = "( P ∧ R ) ↔ ( P ∨ Q )"

print sentence
print

# Byter vissa tecken.
ascii_sentence = sentence
ascii_sentence = re.sub("→", "imp", ascii_sentence)
ascii_sentence = re.sub("∧", "and", ascii_sentence)
ascii_sentence = re.sub("∨", "or",  ascii_sentence)
ascii_sentence = re.sub("↔", "iff", ascii_sentence)
ascii_sentence = re.sub("¬", "neg", ascii_sentence)
ascii_sentence = re.sub("⊢", "con", ascii_sentence)
#sentence = "P imp Q pro neg HelloWorld Q imp P"
 
 
# print ascii_sentence 

# Split every "word", as in space seperated 
atoms = ascii_sentence.split()

num_sente_letters=0
num_connectives=0
used_sent_letters = []
used_sent_letters_indexes = []

is_connective = re.compile('imp|and|or|iff|neg|con')
is_sente_lett = re.compile('[a-zA-Z]')

# full_table = [ [Rådata], [Typ], [Djup], [Sanningsvärde 1], ..., [n] ], [    ]  ]
full_table = []
depth = 0


# print '.------------------------------------'

num_sente_letters = 0
sent_let_truthvalues = [ [ ] ]
temp_inner_values = []
cur_temp_truth_value = 0

# Simply count number of UNIQUE Sentence letters and save num in num_sente_letters
for atom in atoms:
    cur_atom = str(atom)
    if is_sente_lett.match(cur_atom):
        if not is_connective.match(cur_atom):
            if cur_atom not in used_sent_letters:
                # Unique sentence letter was found
                used_sent_letters.append(cur_atom)
                #used_sent_letters_indexes.append()
                
                # print "Found new unique sent letter: " + cur_atom + " num_sente_let: " + str(num_sente_letters)
                num_sente_letters = num_sente_letters + 1
                
                sent_let_truthvalues.append([])
                
                for sent_letter_index in range(0, num_sente_letters):
                    total_inner_length = int(pow(2, num_sente_letters ))
                    sent_let_truthvalues[sent_letter_index] = []
                    
                    for i in range(0, total_inner_length):
                        temp_modulu_i_am_out_of_var_name_ideas = pow(2, sent_letter_index )
                        
                        if i % temp_modulu_i_am_out_of_var_name_ideas == 0:
                            if cur_temp_truth_value == 0:
                                cur_temp_truth_value = 1
                            else:
                                cur_temp_truth_value = 0
                            
                        sent_let_truthvalues[sent_letter_index].append(cur_temp_truth_value)
                        
                
                        
del sent_let_truthvalues[-1]

# DEBUG CODE:
# print sent_let_truthvalues[1]
# print used_sent_letters[1]
# print str(used_sent_letters.index("Q"))
# print "endendendendendendendendendendendendend"

# truth_value = [ 1, 0 ]
# permutaions = itertools.product( truth_value, repeat=num_sente_letters )

neg_was_found = 0
max_depth = 0

# Assign raw, type and depth to each element in sentence and append the full_table 
for atom in atoms:
    cur_atom = str(atom)
    temp_table_element = []
    
    if is_connective.match(cur_atom):
        #print "I: " + str(atom)
        temp_table_element.append(cur_atom)
        if cur_atom == 'neg':
            neg_was_found = 1
        else:
            temp_table_element.append(1)
            temp_table_element.append(depth)
            for truth_val in range(0, total_inner_length):
                temp_table_element.append(-1)
        
            full_table.append(temp_table_element)
            temp_table_element = []
        
    elif cur_atom == '(':
        depth = depth + 1
        if max_depth < depth:
            max_depth = depth
        
    elif cur_atom == ')':
        depth = depth - 1
    
    # All other cases, it's a SENTENCE LETTER:
    else:
        temp_table_element.append(cur_atom)
        sent_let_index=used_sent_letters.index(cur_atom)
        
        if neg_was_found == 1:
            temp_table_element.append(-1)
        else:
            temp_table_element.append(0)
        
        temp_table_element.append(depth)
        
        for truth_val in sent_let_truthvalues[sent_let_index]:
            if neg_was_found == 1:
                if truth_val == 1:
                    truth_val=0
                else:
                    truth_val=1
                
                
            temp_table_element.append(truth_val)
            
        neg_was_found = 0
            
        full_table.append(temp_table_element)
        temp_table_element = []




continue_next_element = 0
skip_this_element = 0
skip_this_element_too = 0
skip_next_loop=1

depth_variation = max_depth

#print "max depth"
#print max_depth

while True: 
    start_at_index = 0   

    #print "CURRENT DEPTH: " + str(depth_variation)

    while True:
        compare_trio_temp=( [] )
        
        for index_temp in range(start_at_index, len(full_table)):
            current_atom_depth=full_table[index_temp][2]
            if current_atom_depth == depth_variation:
                compare_trio_temp.append(full_table[index_temp])
                if len(compare_trio_temp) == 1:
                    left_index=index_temp
                elif len(compare_trio_temp) == 2:
                    middle_index=index_temp
                elif len(compare_trio_temp) == 3:
                    right_index=index_temp
                
            if len(compare_trio_temp) == 3:
                break
        
        start_at_index = index_temp + 1
        
        left_atom=compare_trio_temp[0]
        middle_atom=compare_trio_temp[1]
        right_atom=compare_trio_temp[2]
        
#         print "comparing following:"
#         print str(left_atom) + str(middle_atom) + str(right_atom)
#         print "-"

        if middle_atom[0] == "imp":
            for truth_val in range(0, total_inner_length):
                actual_truth_val = truth_val + 3
                
                if left_atom[actual_truth_val] == 1:
                    if right_atom[actual_truth_val] == 0:
                        full_table[middle_index][actual_truth_val] = 0
                    else:
                        full_table[middle_index][actual_truth_val] = 1
                else:
                    full_table[middle_index][actual_truth_val] = 1
                 
        elif middle_atom[0] == "and":
            for truth_val in range(0, total_inner_length):
                actual_truth_val = truth_val + 3                       
                 
                if left_atom[actual_truth_val] == 1:
                    if right_atom[actual_truth_val] == 1:
                        full_table[middle_index][actual_truth_val] = 1
                    else:
                        full_table[middle_index][actual_truth_val] = 0    
                else:
                    full_table[middle_index][actual_truth_val] = 0
         
        elif middle_atom[0] == "or":
            for truth_val in range(0, total_inner_length):
                actual_truth_val = truth_val + 3                
                 
                if left_atom[actual_truth_val] == 0:
                    if right_atom[actual_truth_val]  == 0:
                        full_table[middle_index][actual_truth_val] = 0
                    else:
                        full_table[middle_index][actual_truth_val] = 1
                else:
                    full_table[middle_index][actual_truth_val] = 1
                     
        elif middle_atom[0] == "iff":
            for truth_val in range(0, total_inner_length):
                actual_truth_val = truth_val + 3                
                 
                if left_atom[actual_truth_val] != right_atom[actual_truth_val] :
                    full_table[middle_index][actual_truth_val] = 0
                else:
                    full_table[middle_index][actual_truth_val] = 1
        
        else:
            print "THIS SHOULDNT HAVE BEEN PRINTED"
        
        full_table[middle_index][2] = depth_variation - 1

        #print str(start_at_index) + "==" + str(len(full_table))
        
        if start_at_index > len(full_table) - 2:
            break
    
    


    if depth_variation == 0:
        break
    
    depth_variation = depth_variation - 1
    #current_atom_array = full_table[index_temp]
    #current_atom_raw=full_table[index_temp][0]
    #current_atom_type=full_table[index_temp][1]
    


# while True: 
#     if depth_variation == 0:
#         break
#     depth_variation = depth_variation - 1
# 
#     
#     print str(depth_variation) + "DEPTH VAR WAS PRINTED HERE"
#     
#     # For every 
#     for index_temp in range(0, len(full_table) - 1):
#         current_atom_depth=full_table[index_temp][2]
#         current_atom_type=full_table[index_temp][1]
#         
#         if full_table[index_temp][2] < 1:
#             continue
#         
#         #print full_table[index_temp]
#         print "DEPTH:" + str(depth_variation) + "  " + str(current_atom_depth)
#         
#         if current_atom_depth != depth_variation:
#             print "SKIP"
#             continue
#            
#         print "Index_temp:" + str(index_temp) + "/" + str(len(full_table))
#         #print full_table
#         
#         if skip_next_loop == 1:
#             skip_next_loop=0
#             continue
# 
#         
#              
#         conn_index = index_temp
#         connective = full_table[conn_index]
#          
#         i=conn_index
#         while True:
#             i = i - 1
#             if full_table[i][2] == depth_variation:
#                 left_let_index=1
#                 break
#         left_let = full_table[left_let_index]    
#         
#         i=conn_index
#         while True:
#             i = i + 1
#             #If it IS a sentence letter, accept it
#             print i
#             if full_table[i][2] == depth_variation:
#                 righ_let_index=1
#                 break
#         righ_let = full_table[righ_let_index]
#         
#         print "comparing following:"
#         print str(left_let) + str(connective) + str(righ_let)
#         print "-"
#         
#         if connective[0] == "imp":
#             for truth_val in range(0, total_inner_length):
#                 actual_truth_val = truth_val + 3
#                 
#                 left_temp_val = left_let[actual_truth_val]
#                 righ_temp_val = righ_let[actual_truth_val]                        
#                 
#                 if left_temp_val == 1:
#                     if righ_temp_val == 0:
#                         full_table[conn_index][actual_truth_val] = 0
#                     else:
#                         full_table[conn_index][actual_truth_val] = 1
#                 else:
#                     full_table[conn_index][actual_truth_val] = 1
#                     
#             full_table[conn_index][2] = depth_variation - 1
#         
#         elif connective[0] == "and":
#             for truth_val in range(0, total_inner_length):
#                 actual_truth_val = truth_val + 3                
#                 
#                 left_temp_val = left_let[actual_truth_val]
#                 righ_temp_val = righ_let[actual_truth_val]           
#                 
#                 if left_temp_val == 1:
#                     if righ_temp_val == 1:
#                         full_table[conn_index][actual_truth_val] = 1
#                     else:
#                         full_table[conn_index][actual_truth_val] = 0    
#                 else:
#                     full_table[conn_index][actual_truth_val] = 0
#         
#         elif connective[0] == "or":
#             for truth_val in range(0, total_inner_length):
#                 actual_truth_val = truth_val + 3                
#                 
#                 left_temp_val = left_let[actual_truth_val]
#                 righ_temp_val = righ_let[actual_truth_val]   
#                 
#                 if left_temp_val == 0:
#                     if righ_temp_val == 0:
#                         full_table[conn_index][actual_truth_val] = 0
#                     else:
#                         full_table[conn_index][actual_truth_val] = 1
#                 else:
#                     full_table[conn_index][actual_truth_val] = 1
#                     
#         elif connective[0] == "iff":
#             for truth_val in range(0, total_inner_length):
#                 actual_truth_val = truth_val + 3                
#                 
#                 left_temp_val = left_let[actual_truth_val]
#                 righ_temp_val = righ_let[actual_truth_val]   
#                 
#                 if left_temp_val != righ_temp_val:
#                     full_table[conn_index][actual_truth_val] = 0
#                 else:
#                     full_table[conn_index][actual_truth_val] = 1
#            
#         depth_temp = depth_variation - 1
#         
#         # Lower the depth of the connective
#         full_table[conn_index][2] = depth_temp
#         
#         
#         
#         print full_table[conn_index]
#         print full_table[left_let_index]
#         print full_table[righ_let_index]
                       
                
                
    

# print "hey"
# #print full_table.index
# print "depth var end"

raw_dat_index = 0

for elem in full_table:
    
    # Byter vissa tecken.
    ascii_sym = full_table[raw_dat_index][0]
    ascii_sym = re.sub("imp", "→", ascii_sym)
    ascii_sym = re.sub("and", "∧",ascii_sym)
    ascii_sym = re.sub("or", "∨", ascii_sym)
    ascii_sym = re.sub("iff", "↔", ascii_sym)
    ascii_sym = re.sub("neg", "¬", ascii_sym)
    ascii_sym = re.sub("con", "⊢", ascii_sym)

    full_table[raw_dat_index][0] = ascii_sym
    raw_dat_index=raw_dat_index+1


# #for child_list in full_table:
print "RESULTS:"
for child_list in full_table:
    if child_list[1] == -1:
        print "¬" + str(child_list[0]) + " ",
    else:
        print " " + str(child_list[0]) + " ",
    
print ""

# print str(total_inner_length) + "HELO"
     
for i in range(0, total_inner_length):
    u=i+3
    for child_list in full_table:
        print " " + str(child_list[u]) + " ",
    
    print "" 
    
# #    print str(child_list[0])
#     print ""

#print str(num_sente_letters)
#print str(used_sent_letters)


#print "Penis one"
skipping = 0
is_valid=0
 
for child_list in full_table:
    if child_list[2] == -1:    
        for i in range(0, total_inner_length):
            u=i+3
            
            if child_list[u] == 0:
                is_valid=0
                break
            else:
                is_valid=1

    
if is_valid == 1:
    print "IT IS VALID!"
else:
    print "IT IS NOT VALID....."
    
    