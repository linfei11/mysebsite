
<template>
  <el-card>
    <el-row>
      <el-col :span="4">
        <el-select
          style="width: 100%"
          v-model="ruleDict.risk_level"
          placeholder="请选择规则等级"
        >
          <el-option label="无风险" value="0"></el-option>
          <el-option label="一般" value="1"></el-option>
          <el-option label="关注" value="2"></el-option>
          <el-option label="严重" value="3"></el-option>
          <el-option label="紧急" value="4"></el-option>
        </el-select>
      </el-col>
      <el-col :span="4">
        <el-select
          style="width: 100%"
          v-model="ruleDict.rule_type"
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
      </el-col>
      <el-col :span="8">
        <el-upload
          class="upload-demo"
          ref="upload"
          action=""
          :on-remove="handleRemove"
          :on-change="handleChange"
          :on-exceed="handleExceed"
          :file-list="fileList"
          :auto-upload="false"
          multiple
          limit="1"
        >
          <template #trigger>
            <el-button type="primary">选取文件</el-button>
          </template>
          <el-button
            style="margin-left: 10px"
            type="success"
            @click="submitUpload"
            >上传到服务器</el-button
          >
          <template #tip>
            <div class="el-upload__tip">只能上传1个文件</div>
          </template>
        </el-upload>
      </el-col>
    </el-row>
  </el-card>
  <el-card>
    <el-table :data="ruleList" style="width: 100%">
      <el-table-column prop="risk_level" label="risk_level" width="180">
      </el-table-column>
      <el-table-column prop="rule_id" label="rule_id" width="180">
      </el-table-column>
      <el-table-column prop="rule_type" label="rule_type"> </el-table-column>
      <el-table-column prop="rule_name" label="rule_name"> </el-table-column>
      <el-table-column prop="content" label="content" show-overflow-tooltip>
      </el-table-column>
      <el-table-column prop="input_type" label="input_type"> </el-table-column>
    </el-table>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      fileList: [],
      localFile: {},
      ruleList: [],
      ruleDict: {
        user: "admin",
        risk_level: "0",
        rule_id: "",
        rule_type: "Trojan",
        rule_name: "",
        content: "",
        comment: "",
        input_type: "1",
        pcap_path: "",
      },
    };
  },
  methods: {
    submitUpload() {
      this.$refs.upload.submit();
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    submitUpload() {
      this.axios({
        url: "attacks/",
        method: "post",
        data: JSON.stringify(this.ruleList),
        headers: { "Content-Type": "application/json" },
        
      }).then((res) => {
        if (res.status !== 201) return this.$message.error("添加规则失败");
        this.$message.success("添加规则成功");
      });
    },
    handleChange(file, fileList) {
      this.localFile = file.raw;
      //console.log(this.localFile)

      let reader = new FileReader();
      reader.readAsText(this.localFile);
      reader.onload = (e) => {
        const filestring = e.target.result;
        //console.log(filestring)

        var ruleArrays = new Array();
        var ruleArray = new Array();
        ruleArrays = filestring.split("\n");

        var j = 0;
        var len = 0;
        for (j = 0, len = ruleArrays.length; j < len; j++) {
          this.ruleDict["content"] = ruleArrays[j];
          ruleArray = ruleArrays[j].split(";").slice(0, -2);
          if (ruleArray.length > 0) {
            this.ruleDict.rule_name = ruleArray[0]
              .split(":")[1]
              .replace('"', "")
              .replace('"', "");
            this.ruleDict.rule_id =
              ruleArray[ruleArray.length - 1].split(":")[1];
            this.ruleList.push({
              user: this.ruleDict.user,
              risk_level: this.ruleDict.risk_level,
              rule_id: this.ruleDict.rule_id,
              rule_type: this.ruleDict.rule_type,
              rule_name: this.ruleDict.rule_name,
              content: this.ruleDict.content,
              comment: this.ruleDict.comment,
              input_type: this.ruleDict.input_type,
              //pcap_path: this.ruleDict.pcap_path,
            });
          }
        }
        console.log(this.ruleList);
      };
    },
    handleExceed(files, fileList) {
      this.$message.warning(
        `当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${
          files.length + fileList.length
        } 个文件`
      );
    },
  },
};
</script>

<style>
</style>


<style lang="less" scoped>
</style>