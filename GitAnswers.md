##1
**Git** is a distributed version control system that allows you to track changes in your files, collaborate on projects, and maintain a complete history of your code locally. **GitLab** is a web-based platform built around Git. It provides a user interface for Git repositories along with additional features such as issue tracking, continuous integration (CI/CD), and project management. Essentially, Git is the tool, while GitLab is a service that leverages Git for collaboration.
##2
**GitLab:** Offers a full DevOps lifecycle platform with built-in CI/CD, and it can be self-hosted. It emphasizes an integrated experience for managing the entire software development lifecycle.
- **GitHub:** Very popular among open-source projects, it provides a robust interface for hosting Git repositories along with social coding features. It has a vast community and many third-party integrations.
- **BitBucket:** Part of the Atlassian suite, BitBucket integrates well with other Atlassian products (like Jira). It supports both Git and Mercurial repositories and is often chosen by teams already using Atlassian’s tools.
##3
 You might use **Git** locally or on a private project where you don't need the additional collaboration features that GitLab offers.
- Git is lightweight and works offline; it doesn’t require a remote server.
- You may prefer to use another platform (such as GitHub or BitBucket) for hosting your repositories, or you might simply manage your version control locally without pushing to a hosted service.
##4Stage your changes:
##   git add <file(s)>
$$**Commit your changes:**  
   `git commit -m "Describe your changes"`
$$ **Push your changes to GitLab:**  
##   git push origin <branch-name>
   
   These steps send your local commits to the remote GitLab repository.
### 5
 A **branch** is a separate line of development within a repository. 
- **Why use branches?**
  - To work on new features or bug fixes without affecting the main (production) code.
  - To isolate experiments or different versions of the project.
 - To enable multiple developers to work in parallel.
##6

   A —— B —— C


     D
     |
A —— B —— C

##7
Give an example of a set of git commands that would result in a merge conflict.
```bash
# Initialize a new repository and create a file
git init
echo "Hello World" > file.txt
git add file.txt
git commit -m "Initial commit"

# Create and switch to a new branch, and modify the file
git checkout -b branch1
echo "Change in branch1" >> file.txt
git commit -am "Update file in branch1"

# Switch back to main, modify the file in a conflicting way
git checkout main
echo "Conflicting change in main" >> file.txt
git commit -am "Update file in main"

# Attempt to merge branch1 into main, triggering a conflict
git merge branch1
##8
Yes
##9
No since git doesnt want binary files
##10
If your local branch is behind the remote branch, Git will reject your push. This is because pushing without pulling could overwrite changes made by others. You would need to pull (and possibly merge or rebase) the remote changes first before pushing.
##11
If you have uncommitted changes, pulling may result in a merge conflict if the remote changes affect the same files. Git might also refuse to pull if your local changes would be overwritten. It’s best to commit or stash your changes before pulling.
##12
A branch is a lightweight pointer within the same repository.
It allows multiple lines of development within the same project.
A fork is a complete copy of a repository, typically used to propose changes to someone else’s project or to use it as a starting point for your own project.
Forks exist as separate repositories, usually under your GitHub (or other platform) account.