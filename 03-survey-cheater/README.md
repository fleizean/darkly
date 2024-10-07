# Survey Voting Cheat / Anket Oylama Hilesi

In the survey page, users can vote for Laurie, Mathieu, Thor, Ly, and Zaz. The purpose of the vote is not explained, so let's assume we are voting for the person with the best shoelaces. Users can add between 1 to 10 points for their chosen person. However, if we look closely at the page's code, we can observe the following:

Anket sayfasında, kullanıcılar Laurie, Mathieu, Thor, Ly ve Zaz için oy kullanabilirler. Oylamanın amacı açıklanmamış, bu yüzden en güzel bağcıkları olan kişi için oy kullandığımızı varsayalım. Kullanıcılar, seçtikleri kişi için 1 ile 10 arasında puan ekleyebilirler. Ancak, sayfanın koduna yakından bakarsak, aşağıdaki durumu gözlemleyebiliriz:

![Survey Cheat](survey-cheat.png)

## Code Example / Kod Örneği

Here is the relevant HTML code:

İşte ilgili HTML kodu:

```html
<td align="center">
    <form action="#" method="post">
        <input type="hidden" name="sujet" value="2">
        <select name="valeur" onchange="javascript:this.form.submit();">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
        </select>
    </form>
</td>
```

These lines are repeated for each person we want to vote for. However, we can modify the `value` attribute of the `option` tags as we wish. Thus, I can add 651665195 points to Thor to make him the top of the leaderboard! (I didn't actually do the math, but the idea is there).

Bu satırlar, oy kullanmak istediğimiz her kişi için tekrarlanır. Ancak, `option` etiketlerinin `value` özniteliğini istediğimiz gibi değiştirebiliriz. Böylece, Thor'a 651665195 puan ekleyerek onu liderlik tablosunun en üstüne çıkarabilirim! (Aslında hesap yapmadım ama fikir bu).

## How to Prevent This? / Bunu Nasıl Önleriz?

To prevent this, you should check the value that a user wants to add on the server side (back-end). In this case, it's easy: the value must be strictly between 1 and 10!

Bunu önlemek için, kullanıcının eklemek istediği değeri sunucu tarafında (back-end) kontrol etmelisiniz. Bu durumda, bu kolay: değer kesinlikle 1 ile 10 arasında olmalıdır!

### Example of Server-Side Validation / Sunucu Tarafı Doğrulama Örneği

Here is an example of how you can validate the value on the server side using PHP:

İşte PHP kullanarak sunucu tarafında değeri nasıl doğrulayabileceğinize dair bir örnek:

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $value = intval($_POST['valeur']);
    if ($value >= 1 && $value <= 10) {
        // Process the vote
        echo "Vote accepted!";
    } else {
        // Invalid vote value
        echo "Invalid vote value!";
    }
}
?>
```

In this example, the value is checked to ensure it is between 1 and 10 before processing the vote.

Bu örnekte, oy işlenmeden önce değerin 1 ile 10 arasında olduğundan emin olmak için kontrol edilir.

## Conclusion / Sonuç

By validating the vote value on the server side, you can prevent users from manipulating the vote values and ensure fair voting.

Oy değerini sunucu tarafında doğrulayarak, kullanıcıların oy değerlerini manipüle etmelerini önleyebilir ve adil oylamayı sağlayabilirsiniz.