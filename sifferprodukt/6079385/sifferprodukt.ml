let rec digitProd n =
    match n with
    | 0 -> 1
    | _ -> (if (n mod 10) = 0 then 1 else (n mod 10)) * digitProd (n / 10)
;;

let _ =
    let rec getFinalDigit n =
        if n < 10 then n else getFinalDigit (digitProd n) in
    print_int (getFinalDigit (read_int()))
;;