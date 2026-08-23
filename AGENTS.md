# Playground Rules

When the user asks to setup a playground or boilerplate for a problem:
- **NEVER** propose or provide the actual solution in the playground code.
- Only provide the class definition, empty function signatures (with `pass` or `raise NotImplementedError`), and necessary test cases so the user can implement it themselves.
- **ALWAYS** include a programmatic check comparing the actual output against the expected output in the test cases, printing whether the test passed or failed.
- **ALWAYS** deduce the core Data Structure/Algorithm topic of the provided problem (e.g., sliding-window, dynamic-programming, graphs, etc.) on your own and create/place the playground file in a corresponding topic-wise folder within the workspace.
- **ALWAYS** update the `README.md` file whenever you set up a playground. Ensure the `README.md` is professional, appealing, informative, and well-structured per guidelines. It should include an index table with columns "Problem Title" (with a hyperlink to the LeetCode problem) and "View" (with a hyperlink to the local playground file in the repository).
