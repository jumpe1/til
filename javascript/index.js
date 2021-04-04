// function isTweetable(text) {
//     return text.length <= 140;
// }

// 関数式：匿名（無名）関数
const isTweetable = function (text) {
    return text.length <= 140;
}

console.log(isTweetable("foo"));

// 高階関数
function confirmed(fn) {
    if (window.confirm("実行しますか？")) {
        fn();
    }
}

function unfollow() {
    console.log("フォローを外しました");
}

// function cancelTweet() {
const cancelTweet = function () {
    console.log("ツイートをキャンセルしました");
}

confirmed(unfollow)
confirmed(cancelTweet)

// 高階関数2
function confirmed2(fn) {
    const input = window.prompt("実行しますか？");
    fn(input);
}

confirmed2(function (input) {
    if (input === "実行") {
        console.log("リポジトリを削除");
    }
})

// const btn = document.getElementById("button");
// btn.addEventListener("click", function () {
//     console.log("フォロー解除");
// })

const foods = ["にんじん", "じゃがいも", "玉ねぎ"];
foods.forEach(function (food) {
    console.log(food);
})

// Web APIを叩く サンプル
// asyncをつけると非同期関数となる
async function callApi() {
    // fetchでpromiseオブジェクトが返ってくる(async + awaitではない場合）
    // async + awaitを使うとResponseオブジェクトが返ってくる
    const res = await window.fetch('https://jsonplaceholder.typicode.com/posts');
    const users = await res.json();
    console.log(users);
}

callApi();