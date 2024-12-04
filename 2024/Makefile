DAY=1
MAIN=aoc$(DAY)
TOOLS=aoctools.c

main: aoc$(DAY).c
	gcc -Wall -Wextra -fsanitize=address,undefined -o $(MAIN) $(MAIN).c $(TOOLS) -g

run:
	./$(MAIN)
