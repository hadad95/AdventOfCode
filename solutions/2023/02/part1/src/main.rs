use std::fs;

fn main() {
    let txt: String = fs::read_to_string("../input.txt").expect("Should have opened the input file");
    let mut result: i32 = 0;
    for (id, line) in txt.lines().enumerate() {
        let games = &line[line.find(":").unwrap()+1..].trim();
        let hands: Vec<&str> = games.split(";").map(|x: &str| x.trim()).collect::<Vec<&str>>();
        let mut impossible: bool = false;
        for hand in hands {
            let info: Vec<&str> = hand.split(",").map(|x: &str| x.trim()).collect::<Vec<&str>>();
            for combo in info {
                let ball: Vec<&str> = combo.split(" ").collect::<Vec<&str>>();
                let num: i32 = ball[0].parse::<i32>().unwrap();
                let color: &str = ball[1];
                if (color == "red" && num > 12) || (color == "green" && num > 13) || (color == "blue" && num > 14) {
                    impossible = true;
                    break;
                }
            }
            if impossible {
                break
            }
        }
        if !impossible {
            result += id as i32 + 1;
        }
    }
    println!("{}", result);
}
