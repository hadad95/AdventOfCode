use std::fs;
use std::cmp;

fn main() {
    let txt: String = fs::read_to_string("../input.txt").expect("Should have opened the input file");
    let mut result: i32 = 0;
    for line in txt.lines() {
        let games = line[line.find(":").unwrap()+1..].trim();
        let hands: Vec<&str> = games.split(";").map(|x: &str| x.trim()).collect::<Vec<&str>>();
        let mut r: i32 = 0;
        let mut g: i32 = 0;
        let mut b: i32 = 0;
        for hand in hands {
            let info: Vec<&str> = hand.split(",").map(|x: &str| x.trim()).collect::<Vec<&str>>();
            for combo in info {
                let ball: Vec<&str> = combo.split(" ").collect::<Vec<&str>>();
                let num: i32 = ball[0].parse::<i32>().unwrap();
                let color: &str = ball[1];
                match color {
                    "red" => r = cmp::max(r, num),
                    "green" => g = cmp::max(g, num),
                    "blue" => b = cmp::max(b, num),
                    _ => ()
                }
            }
        }
        result += r * g * b;
    }
    println!("{}", result);
}
