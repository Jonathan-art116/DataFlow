# DataFlow
Tools for general purpose data flow.




## How to commit. 
### commit message
***
<`type`>(<`scope`>): <`subject`>
***
- type(**must**)
  - feat: feature
  - fix/to: fix bug
    - fix: Generate a diff and fix this automatically. Suitable for direct fixes in one commit
    - to: Just generating a diff does not automatically fix this problem. Good for multiple commits. Use fix when submitting final fixes
  - docs: documentation
  - style: format code.
  - refactor: refactor coe.
  - perf: Optimization related, such as improving performance and experience.
  - test: add tests.
  - chore: Changes to the build process or accessibility tools.
  - revert: Roll back to a previous version.
  - merge: code merge commit
  - sync: Sync bugs on mainline or branch.
- scope(optional)
  - Scope is used to illustrate the scope of commit influence, such as data layer, control layer, view layer, etc., depending on the project.
- subject(**must**)
  - subject is a brief description of the purpose of the commit, no more than 50 characters.
  > Do not end with a period or other punctuation.
  - examples:
  > fix(DAO):User query is missing username attribute  
  > feat(Controller):User query interface development