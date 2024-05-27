package com.cums.user;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.User;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RequiredArgsConstructor
@Controller
@RequestMapping("/user")
public class UserController {
    private final UserService userService;
    @GetMapping("/signup")
    public String signup(UserCreateForm userCreateForm){
        return "signup_form";
    }
    @PostMapping("/signup")
    public String signup(@Valid UserCreateForm userCreateForm, BindingResult bindingResult){
        if(bindingResult.hasErrors()){
            return "signup_form";
        }
        //bindingResult.rejectValue(필드명, 오류 코드, 오류 메시지)
        if(!userCreateForm.getPassword1().equals(userCreateForm.getPassword2())){
            bindingResult.rejectValue("password2","passwordInCorrect",
                "2개의 패스워드가 일치하지 않습니다.");
            return "signup_form";
        }
        /**
         * 이미 등록된 사용자 처리
         */
        try {
            userService.create(userCreateForm.getUsername(),
            userCreateForm.getEmail(), userCreateForm.getPassword1(),userCreateForm.getNickname());

        }catch(DataIntegrityViolationException e) {
            e.printStackTrace();
            bindingResult.reject("signupFailed", "이미 등록된 사용자입니다.");
            return "signup_form";
        }catch(Exception e) {
            e.printStackTrace();
            bindingResult.reject("signupFailed", e.getMessage());
            return "signup_form";
        }
        return "redirect:/";
    }

    @GetMapping("/login")
    public String login(){
        return "login_form";
    }

    @PostMapping("/updateNickname") //이름 변경
    public String updateNickname(@AuthenticationPrincipal User principal, @RequestParam String newNickname) {
        String username = principal.getUsername();
        userService.updateNickname(username, newNickname);
        return "myInfo";
    }
    @GetMapping("/update_nickname") //이름 변경
    public String showUpdateNicknameForm() {
        return "update_nickname"; // update_nickname.html의 이름
    }
}