# 注意点

- 名詞と動詞をセットで書き出す
- ドメインで切り分けてエンティティの抽出を行う
- エンティティ or 値オブジェクトかを意識する


# フェーズ1 エンティティ抽出

## CustomUser
- id
- employeeNo
- firstName
- middleName
- lastName
- sex
- birth_date
- email
- postcode
- prefecture
- city
- address1
- address2
- password
- role
- tel
- createdAt
- updatedAt
- isActive

## departments (自己参照)
- id
- name
- parentId (departments.id)
- createdAt
- updatedAt
- isActive

## user_department (中間テーブル)
- userId
- departmentId

## roles
- id
- role
- createdAt
- UpdatedAt
- isActive

## daily_reports
- id
- userId
- title
- content
- createdAt
- updatedAt
- status(textchoice)

## tags
- id
- name
- createdAt

## report_tags
- reportId
- tagId

## templates
- id
- departmentId
- contentLayout
- createdAt
- updatedAt
- isActive