<template>
  <div class="create_container">
    <el-form
      ref="formRef"
      :model="create_form"
      label-width="100px"
      label-position="left"
    >
      <el-form-item
        label="规则添加者"
        prop="user"
        :rules="[
          { required: true, message: '用户名不能为空' },
          { min: 1, max: 50, message: '长度在 1 到 50 个字符' },
        ]"
      >
        <el-input v-model="create_form.user"></el-input>
      </el-form-item>
      <el-form-item
        label="规则等级"
        prop="risk_level"
        :rules="[{ required: true, message: '规则等级不能为空' }]"
      >
        <el-select
          style="width: 100%"
          v-model="create_form.risk_level"
          placeholder="请选择规则等级"
        >
          <el-option label="无风险" :value="0"></el-option>
          <el-option label="一般" :value="1"></el-option>
          <el-option label="关注" :value="2"></el-option>
          <el-option label="严重" :value="3"></el-option>
          <el-option label="紧急" :value="4"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="导入类型" prop="input_type">
        <el-select
          style="width: 100%"
          v-model="create_form.input_type"
          placeholder="请选择导入类型"
        >
          <el-option label="批量导入" :value="1"></el-option>
          <el-option label="手动添加" :value="2"></el-option>
          <el-option label="自动收集" :value="3"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item
        label="规则类型"
        prop="rule_type"
        :rules="[{ required: true, message: '规则类型不能为空' }]"
      >
        <el-select
          style="width: 100%"
          v-model="create_form.rule_type"
          placeholder="请选择规则类型"
        >
          <el-option label="普通木马" value="Trojan"></el-option>
          <el-option label="QM木马" value="QM_Trojan"></el-option>
          <el-option label="漏洞利用" value="Exploit"></el-option>
          <el-option label="恶意IP" value="Black_IP"></el-option>
          <el-option label="恶意域名" value="Black_Domain"></el-option>
          <el-option label="恶意URL" value="Black_URL"></el-option>
          <el-option label="恶意邮箱" value="Black_Mail"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item
        label="规则id "
        prop="rule_id"
        :rules="[
          { required: true, message: '规则id不能为空' },
          { min: 1, max: 100, message: '长度在 1 到 100 个字符' },
        ]"
      >
        <el-input v-model="create_form.rule_id" placeholder="规则id根据规则内容自动生成，请输入规则内容"></el-input>
      </el-form-item>
      <el-form-item label="规则名" prop="rule_name">
        <el-input v-model="create_form.rule_name"
        placeholder="规则名根据规则内容自动生成，请输入规则内容"></el-input>
      </el-form-item>
      <el-form-item
        label="规则内容 "
        prop="content"
        :rules="[
          { required: true, message: '规则内容不能为空' },
          { min: 1, max: 1000, message: '长度在 1 到 1000 个字符' },
        ]"
      >
        <el-input
          v-model="create_form.content"
          @change="contentChange"
        ></el-input>
      </el-form-item>
      <el-form-item label="pcap文件" prop="pcap_path">
        <el-card>
          <el-tooltip effect="dark" placement="top" :content="create_form.pcap_path"
          :disabled="create_form.pcap_path == null">
          <el-upload
            ref="upload"
            drag
            class="upload-demo"
            action="http://127.0.0.1:8001/attacks/"
            :auto-upload="false"
            :data="create_form"
            :on-success="onSuccess"
            :on-change="handleChange"
            name="pcap_path"
            style="padding: 10px"
          >
            <i class="el-icon-upload" />
            <div class="el-upload__text">
              将文件拖到此处，或<em>点击上传</em>
            </div>
          </el-upload>
          </el-tooltip>
        </el-card>
      </el-form-item>
      <el-form-item label="用户评论" prop="comment">
        <el-input v-model="create_form.comment"></el-input>
      </el-form-item>
      <el-form-item size="large">
        <el-button type="primary" @click="submitUpload">立即修改</el-button>
        <el-button @click="resetForm">恢复原始内容</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "Create",
  props: ["create_form"],
  methods: {
    contentChange() {
      //console.log(this.create_form.content)
      var teststr = this.create_form.content;
      var myArray = new Array();
      myArray = teststr.split(";").slice(0, -2);
      this.create_form.rule_name = myArray[0]
        .split(":")[1]
        .replace('"', "")
        .replace('"', "");
      this.create_form.rule_id = myArray[myArray.length - 1].split(":")[1];
      //console.log(this.create_form.rule_name);
      //console.log(this.create_form.rule_id);
    },
    onSuccess() {
      this.$message.success("upload success");
    },
    handleChange(file) {
      this.isFileExist = true;
    },
    submitUpload() {
      this.$refs.formRef.validate((valid) => {
        if (!valid) {
          this.$alert("有未填写字段", "提示", {
            confirmButtonText: "确定",
          });
        } else {
          if (this.isFileExist) {
            this.$refs.upload.submit();
          } else {
            this.onSubmit();
          }
        }
      });
    },
    onSubmit() {
      this.$refs.formRef.validate((valid) => {
        if (!valid) {
          this.$alert("有未填写字段", "提示", {
            confirmButtonText: "确定",
          });
        } else {
          console.log(this.create_form);
          this.axios({
            url: "attacks/" + this.create_form.id + "/",
            method: "put",
            data: this.create_form,
            headers: { "Content-Type": "application/json" },
          }).then((res) => {
            if (res.status !== 200) return this.$message.error("修改规则失败");
            this.$message.success("修改规则成功");
          });
        }
      });
    },
    resetForm() {
      this.$refs.formRef.resetFields();
    },
  },
};
</script>
<style lang="less" scoped>
</style>
