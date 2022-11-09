/*

    Tri selection (tableau) :
        On déclare une variable minimum
        On parcours le tableau -1:

            mini <- index de l'élément actuel
            On re parcours le tableau :

                si tableau[mini] > tableau[mini+1] :
                    mini <- mini+1
                Fin de si

            Fin du parcours

            Si l'élément actuel est différent de tabeleau[mini] :
                échange de l'élément actuel du tableau avec tableau[mini]
            Fin de si

        Fin du parcours

        On affiche le tableau trié

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
    for (let i = 0; i < array.length-1; i++) {
        let minimum = i;
        cpt++
        for (let j = i+1; j < array.length; j++) {
            cpt++
            if(array[minimum] > array[j]){
                minimum = j;
                cpt++
            }
        }
        cpt++
        if(array[i] != array[minimum]){
            let temp = array[i];
            array[i] = array[minimum];
            array[minimum] = temp;
            cpt+= 3
        }
    }
    console.log(array);
    return cpt;
}
