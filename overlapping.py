import sys
seqa_begin = int(sys.argv[1])
seqa_end = int(sys.argv[2])
seqb_begin = int(sys.argv[3])
seqb_end = int(sys.argv[4])

if (seqa_begin <= seqb_begin and seqa_end <= seqb_end and seqa_end >= seqb_begin ) or (seqa_begin <= seqb_begin and seqa_end >= seqb_end and seqa_end >= seqb_begin ) or (seqb_begin <= seqa_begin and seqb_end <= seqa_end and seqa_begin <= seqb_end ) or (seqa_begin >= seqb_begin and seqa_end >= seqb_end and seqb_begin >= seqa_end ):
 print("overlap")
 
else:
 print("not overlap")









