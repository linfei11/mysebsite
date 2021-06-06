<template>
    <div class="login_container">
        <div class="login_box">
          <div class="avatar_box">
            <img src="../assets/logo.png" alt="">
          </div>
          <el-form ref="loginFormRef" :model="login_form" class="login_form" :rules="rules">
            <!--user name-->
            <el-form-item prop="username">
              <el-input v-model="login_form.username" prefix-icon="el-icon-user"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input v-model="login_form.password" prefix-icon="el-icon-unlock" type="password"></el-input>
            </el-form-item>
            <el-form-item class="btns">
               <el-button type="primary" @click="login">login</el-button>
                <el-button type="info" @click="resetLoginForm">reset</el-button>
            </el-form-item>
          </el-form>
        </div>
    </div>
</template>
<script>
export default {
  name: 'login',
  data () {
    return {
      login_form: {
        username: 'xiaoming',
        password: '123'
      },
      rules: {
        username: [
          { required: true, message: '请输入活动名称', trigger: 'blur' },
          { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ],
        password: []
      }
    }
  },
  methods: {
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      this.$refs.loginFormRef.validate(valid => {
        if (!valid) {
          return false
        }
      })
    }
  }

}
</script>
<style lang="less" scoped>
.login_container{
  background-color: #2b4b6b;
  height: 100%;
}

.login_box{
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);

  .avatar_box{
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;

    img {
      height: 100%;
      width: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
}

.btns{
  display: flex;
  justify-content: flex-end;
}

.login_form{
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>
