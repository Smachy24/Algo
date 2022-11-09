/*

    Tri selection (tableau) :
        On déclare une variable minimum
        On parcours le tableau:

            mini <- index de l'élément actuel
            On re parcours le tableau :

                si tableau[mini] > tableau[mini+1] :
                    mini <- mini+1

            Fin du parcours

            échange de l'élément actuel du tableau avec tableau[minimum]

        Fin du parcours

        On renvoie le tableau trié

    Fin du tri.

    Test : 
        (entré) tableau = [3, 10, 1, 8, 2, 4, 5, 10, 3]
        selection(tableau)
        >>> (sortie) [1,2,3,3,4,5,8,10,10]

    Dans le meilleur de cas :
        tableau = [1,2,3,4,5,6,7,8,10,9]
        selection(tableau)
        >>> [1,2,3,4,5,6,7,8,9,10] en 41 opérations
    
    Dans le pire de cas : 
        tableau = [10,9,8,7,6,5,4,3,2,1]
        selection(tableau)
        >>> [1,2,3,4,5,6,7,8,9,10] en 65 opérations
*/

function selectionSort (array){
    let cpt = 0;
    for (let i = 0; i < array.length; i++) {
        let minimum = i;
        for (let j = i+1; j < array.length; j++) {
            if(array[minimum] > array[j]){
                minimum = j;
                cpt++
            }
        }
        let temp = array[i];
        array[i] = array[minimum];
        array[minimum] = temp;
        cpt+= 3
    }
    return [array, cpt];
}

/* ========== Méthodes stats =========== */

function stats (min, max, step, nbr){
    let stepCpt = 0;
    for (let i = 0; i <= nbr; i++) {
        let array = [];
        for (let j = 0; j < Math.floor(Math.random() * (max-min) + min + stepCpt); j++) {
            let randomNumber = Math.floor(Math.random() * 100);
            array.push(randomNumber);
            stepCpt+= step;
        }

    }


}