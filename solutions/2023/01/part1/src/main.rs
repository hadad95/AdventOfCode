use std::fs;

fn main() {
    let txt: String = fs::read_to_string("../input.txt").expect("Should have read the file");
    let mut result:i32 = 0;
    for line in txt.lines() {
        let mut first_digit: i32 = 0;
        let mut last_digit: i32 = 0;
        for c in line.chars() {
            if c.is_digit(10) {
                let num: i32 = c.to_string().parse::<i32>().unwrap();
                if first_digit == 0 {
                    first_digit = num;
                }
                last_digit = num;
            }
        }
        result += (first_digit * 10) + last_digit;
    }
    println!("{}", result);
}
