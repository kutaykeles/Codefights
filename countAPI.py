import collections
def countAPI(calls):
	hm=collections.OrderedDict()
	hm2=collections.OrderedDict()
	hm3=collections.OrderedDict()
	final=[]
	final2=[]
	for call in calls:
		c = call[1:].split("/")
		if(c[0] not in hm):
			ar=[]
			ar.append(c[0])
			hm[c[0]] = len(ar)
		else:
			hm[c[0]] += len(ar)
		key=c[0] + "/" + c[1]
		if(key not in hm2):
			ar=[]
			ar.append(key)
			hm2[key] = len(ar)
		else:
			hm2[key] += len(ar)
		key2=c[0] + "/" + c[1] + "/" + c[2]
		if(key2 not in hm3):
			ar=[]
			ar.append(key2)
			hm3[key2] = len(ar)
		else:
			hm3[key2] += len(ar)

	for f in hm:
		final.append("--"+f+" (%d)"%(hm[f]))
		for f2 in hm2:
			c= f2.split("/")
			if(f+"/" in f2):
				final.append("----"+c[1]+" (%d)"%(hm2[f2]))
				for f3 in hm3:
					c=f3.split("/")
					if(f2+"/" in f3):
						final.append("------"+c[2]+" (%d)"%(hm3[f3]))
	return(final)
			
		
	
	
	
countAPI(["/project5/subproject2/method5", 
 "/project3/subproject5/method4", 
 "/project4/subproject1/method4", 
 "/project4/subproject3/method3", 
 "/project5/subproject1/method2", 
 "/project2/subproject2/method1", 
 "/project3/subproject1/method4", 
 "/project1/subproject2/method5", 
 "/project2/subproject1/method2", 
 "/project1/subproject3/method3", 
 "/project2/subproject1/method8", 
 "/project3/subproject3/method3", 
 "/project1/subproject1/method10", 
 "/project1/subproject3/method3", 
 "/project2/subproject1/method9", 
 "/project5/subproject2/method3", 
 "/project5/subproject2/method5", 
 "/project5/subproject1/method7", 
 "/project5/subproject1/method9", 
 "/project1/subproject1/method5"])



#["--project1 (6)", 
#"----subproject1 (3)", 
#"------method1 (2)", 
#"------method2 (1)", 
#"----subproject2 (3)", 
#"------method1 (3)", 
#"--project2 (2)", 
# "----subproject1 (2)", 
# "------method1 (2)"]
