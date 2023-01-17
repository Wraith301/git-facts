<h2>git-facts utility tool</h2>
<p>The tool shows the following facts about a local git repository.</p>
<ul>
<li>The current active branch in the local repository</li>
<li>Whether repository files have been modified</li>
<li>Whether the current head commit was authored in the last week</li>
<li>Whether the current head commit was authored by Rufus</li>
</ul>


<p>Dependencies:</p>
<ul>
<li>git</li>
<li>python3</li>
</ul>

<p>python libraries</p>
<p> Install python3 and git from their official website. "subprocess", "datetime" and "argparse" should already be installed with standard python, but if not then use:

    pip install subprocess
    pip install datetime
    pip install argparse

<h3>Instructions to run</h3>
<p>In a command line, navigate to the directory containing the script. Use the following command to run the script.</p>

    python git-facts.py --path "<local_git_repository_absolute_path>"
