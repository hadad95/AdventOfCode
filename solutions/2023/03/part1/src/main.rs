use std::fs;

fn is_symbol(c: char) -> bool {
    !c.is_numeric() && !(c == '.')
}

fn check_vec(pos: usize, line: &Vec<char>) -> bool {
    !line.is_empty() && (is_symbol(line[pos]) || (pos != 0 && is_symbol(line[pos - 1])) || (pos < line.len() - 1 && is_symbol(line[pos + 1])))
}

fn check_validity(pos: usize, line: &Vec<char>, before: &Vec<char>, after: &Vec<char>) -> bool {
    check_vec(pos, line) || check_vec(pos, before) || check_vec(pos, after)
}

fn main() {
    let data: String = fs::read_to_string("../input.txt").expect("Should have read the file");
    let mut sum: i32 = 0;
    let lines: Vec<&str> = data.lines().collect::<Vec<&str>>();
    for (i, line) in lines.iter().enumerate() {
        let mut valid: bool = false;
        let mut num: i32 = 0;
        for (j, c) in line.chars().enumerate() {
            if c.is_numeric() {
                num *= 10;
                num += c.to_digit(10).unwrap() as i32;
                if !valid {
                    let before: Vec<char> = if i == 0 { Vec::<char>::new() } else { lines[i - 1].chars().collect::<Vec<char>>() };
                    let after: Vec<char> = if i == lines.len() - 1 { Vec::<char>::new() } else { lines[i + 1].chars().collect::<Vec<char>>() };
                    let curr_line: Vec<char> = line.chars().collect::<Vec<char>>();
                    valid = check_validity(j, &curr_line, &before, &after);
                }
                if j == line.len() - 1 && valid {
                    sum += num;
                    valid = false;
                }
            }
            else {
                if valid {
                    sum += num;
                    valid = false;
                }
                num = 0;
            }
        }
    }
    println!("{}", sum);
}
