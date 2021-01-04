<template>
    <div>
        <table>
            <tr>
                <td>编号</td>
                <td>图书名称</td>
                <td>作者</td>
            </tr>
            <tr v-for="item in books">
                <td>{{item.id}}</td>
                <td>{{item.name}}</td>
                <td>{{item.author}}</td>
            </tr>
        </table>
        {{msg}}
    </div>
</template>

<script>
    export default {
        name: "Book",
        data() {
            return {
                msg: 'Hello Vue',
                books: [
                    {
                        id: 1,
                        name: 'Java',
                        author: 'Luke'
                    },
                    {
                        id: 2,
                        name: 'Python',
                        author: 'Mike'
                    },
                    {
                        id: 3,
                        name: 'Vue',
                        author: 'Lily'
                    }
                ]
            }
        }
    }
</script>

<style scoped>

</style>