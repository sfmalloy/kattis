fun main(args : Array<String>) {
    var moves = readLine()
    var ball = intArrayOf(1,0,0)

    for (i in 0 until moves!!.length) {
        when (moves.get(i)) {
            'A' -> ball[0] = ball[1].also{ ball[1] = ball[0] }
            'B' -> ball[1] = ball[2].also{ ball[2] = ball[1] }
            else -> ball[0] = ball[2].also{ ball[2] = ball[0] }
        }
    }

    for (i in 0 until ball.size) {
        if (ball[i] == 1) {
            println(i + 1)
            break
        }
    }
}
