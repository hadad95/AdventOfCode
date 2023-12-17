use std::cmp;
use std::collections::HashMap;
use std::fs;

fn is_asterisk(c: char) -> bool {
    c == '*'
}

fn find_asterisk(pos: usize, line: &Vec<char>) -> i32 {
    if line.is_empty() {
        -1
    } else if is_asterisk(line[pos]) {
        pos as i32
    } else if pos != 0 && is_asterisk(line[pos - 1]) {
        (pos - 1) as i32
    } else if pos < line.len() - 1 && is_asterisk(line[pos + 1]) {
        (pos + 1) as i32
    } else {
        -1
    }
}

fn main() {
    let data: String = fs::read_to_string("../input.txt").expect("Should have read the file");
    let lines: Vec<&str> = data.lines().collect::<Vec<&str>>();
    let mut map: HashMap<String, Vec<i32>> = HashMap::<String, Vec<i32>>::new();
    let mut sum: i32 = 0;
    for (i, line) in lines.iter().enumerate() {
        let mut found_asterisks: Vec<String> = vec![];
        let mut num: i32 = 0;
        for (j, c) in line.chars().enumerate() {
            if c.is_numeric() {
                num *= 10;
                num += c.to_digit(10).unwrap() as i32;

                let before: Vec<char> = if i == 0 {
                    Vec::<char>::new()
                } else {
                    lines[i - 1].chars().collect::<Vec<char>>()
                };

                let after: Vec<char> = if i == lines.len() - 1 {
                    Vec::<char>::new()
                } else {
                    lines[i + 1].chars().collect::<Vec<char>>()
                };

                let curr_line: Vec<char> = line.chars().collect::<Vec<char>>();
                let possible_before: i32 = find_asterisk(j, &before);
                let possible_curr: i32 = find_asterisk(j, &curr_line);
                let possible_after: i32 = find_asterisk(j, &after);
                let possible_y: i32 = if possible_before > -1 { i as i32 - 1 } else if possible_curr > -1 { i as i32 } else if possible_after > -1 { i as i32 + 1} else { -1 };
                let possible_x: i32 = cmp::max(possible_before, cmp::max(possible_curr, possible_after));
                if possible_x > -1 && !found_asterisks.contains(&format!("{},{}", possible_y, possible_x))
                {
                    let found: String = format!("{},{}", possible_y, possible_x);
                    if !found_asterisks.contains(&found) {
                        found_asterisks.push(found);
                    }
                }

                if j == line.len() - 1 {
                    for found in &found_asterisks {
                        map.entry(found.to_string()).and_modify(|v| v.push(num)).or_insert(vec![num]);
                    }
                }
            } else {
                if num == 0 {
                    continue;
                }

                for found in &found_asterisks {
                    map.entry(found.to_string()).and_modify(|v| v.push(num)).or_insert(vec![num]);
                }
                num = 0;
                found_asterisks.clear();
            }
        }
    }

    for (_, val) in map.iter() {
        if val.len() != 2 {
            continue;
        }

        let result: i32 = val.iter().product();
        sum += result;
    }
    println!("{}", sum);
}
