 ; I am really confused about this part, but the assignment said not to worry about it.
 (defn cartesian-product
      ([] '(()))
      ([xs & more]
        (mapcat #(map (partial cons %)
                      (apply cartesian-product more))
                xs)))

 ; define the lists 
 (def flavorslistnumber1 ["Vanilla" "Chocolate" "Cherry-Ripple"])
 (def flavorslistnumber2 ["Lemon" "Butterscotch" "Licorice-Ripple"])
 (def combinedflavors (concat flavorslistnumber1 flavorslistnumber2))

 ; main function that filters the different combinations of ice cream flavors
 (defn main []
    ; pass in to cartesian-product the two seperate lists
   (println "Lists Results: ")
   (println
     (filter
       #(= (first %) "Chocolate")
       (cartesian-product flavorslistnumber1 flavorslistnumber2)))
    ; pass in to cartesian-product the combined lists
   (println "Second List Results: ")
   (println
      (filter
        #(or (= (first %) "Chocolate") (= (last %) "Chocolate"))
       (cartesian-product combinedflavors combinedflavors))))

 (main)