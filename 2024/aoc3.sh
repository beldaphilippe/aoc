#Part 1
cat input.txt | grep -o 'mul([0-9][0-9]*,[0-9][0-9]*)' | sed 's/mul(//g' | sed 's/,/ /g' | sed 's/)/*p/g' | dc | awk '{ sum += $1 } END { print sum }'

# Part 2
cat input.txt | grep -o -E "do\(\)|don't\(\)|mul\([0-9][0-9]*,[0-9][0-9]*\)" | tr -d '\n' | perl -p -e "s/don't\(\).*?do\(\)/do\(\)/g" | grep -o 'mul([0-9][0-9]*,[0-9][0-9]*)' | sed 's/mul(//g' | sed 's/,/ /g' | sed 's/)/*p/g' | dc | awk '{ sum += $1 } END { print sum }'
