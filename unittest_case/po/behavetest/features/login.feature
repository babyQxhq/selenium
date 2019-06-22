#coding=utf-8
Feature: Login User

    As a developer
    This is my first bdd project
    #场景1
    Scenario:open login website
        When I open the login website "http://www.maiziedu.com/"
        Then I expect that the title is "麦子学院"
    #场景2
    Scenario:input username
        When I set with username "15210424367"
        And I set with password "1234567"
        And I click with login
        Then I except that text "账号或者密码错误，请重新输入"
