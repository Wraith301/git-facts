import subprocess
import datetime
import argparse

def git_info(git_dir):
	# active branch
	active_branch = subprocess.run(['git','branch','--show-current'], capture_output=True, text=True, cwd=git_dir)

	# local changes
	local_changes=False
	local_changes_check = subprocess.run(['git','status','--porcelain'], capture_output=True, text=True, cwd=git_dir)
	if local_changes_check.stdout:
		local_changes=True
	

	# whether the current head commit was authored in the last week
	last_week=False
	try:
		last_week_check = subprocess.run(['git','log','-1','--date=iso'], capture_output=True, text=True, cwd=git_dir)
		holder=last_week_check.stdout.strip().split() #extracting information into a list of strings
		for i,date in enumerate(holder): #finding the required string index
			if date=='Date:':
				indexd=i
		holder1=holder[indexd+1:indexd+1+2]
		commit_date=holder1[0].split('-')
		commit_time=holder1[1].split(':')
		commit_datetime=datetime.datetime(int(commit_date[0]),int(commit_date[1]),int(commit_date[2]),int(commit_time[0]),int(commit_time[1]),int(commit_time[2]))
		current_datetime=datetime.datetime.now()
		diff=current_datetime-commit_datetime


		if 'day' in str(diff):
			if int(str(diff).split()[0])<7:
				last_week=True
		else:
			last_week=True
	except: #if the repository has no commits
		pass

	# whether the current head commit was authored by Rufus
	by_Rufus=False
	try:
		for j,author in enumerate(holder): #finding the required string index
			if author=='Author:':
				indexa=j
		holder2=holder[indexa+1:indexa+2]
		if holder2=='Rufus':
			by_Rufus=True
	except: #if the repository has no commits
		pass

	print('active branch: {}'.format(active_branch.stdout.strip()))
	print('local changes: {}'.format(local_changes))
	print('recent commit: {}'.format(last_week))
	print('blame Rufus: {}'.format(by_Rufus))

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', type=str, required=True, help='enter the path to your local git repository')
	args=parser.parse_args()
	git_dir=args.path
	git_info(git_dir)