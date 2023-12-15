use std::fs;

fn main() {
    let txt: String = fs::read_to_string("../input.txt").expect("Should have read the file");
    let numbers = vec!["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let mut result:i32 = 0;
    for line in txt.lines() {
        let mut first_digit: i32 = 0;
        let mut last_digit: i32 = 0;
        for (i, c) in line.chars().enumerate() {
            if c.is_digit(10) {
                let parsed: i32 = c.to_string().parse::<i32>().unwrap();
                if first_digit == 0 {
                    first_digit = parsed;
                }
                last_digit = parsed;
            }
            else {
                for (j, num) in numbers.iter().enumerate() {
                    if num.starts_with(c) && num.len() <= line.len()-i && &line[i..i+num.len()] == *num {
                        if first_digit == 0 {
                            first_digit = j as i32;
                        }
                        last_digit = j as i32;
                    }
                }
            }
        }
        result += (first_digit * 10) + last_digit;
    }
    println!("{}", result);
}
