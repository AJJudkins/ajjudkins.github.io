(fn [x y]
   (loop [a x b y gcd 0]
     (if (= b 0)
       gcd
       (if (< a b)
        (recur b a gcd)
        (recur b (rem a b) b)))))

;(defn gcd [a b]
 ; (if (zero? b) a
  ;(gcd b (mod a b))))