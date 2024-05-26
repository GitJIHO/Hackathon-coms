package com.cums;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @GetMapping("/redirectToDiary")
    public String redirectToDiary() {
        return "redirect:/diary";
    }

    @GetMapping("/redirectToDiaryAnalysis")
    public String redirectToDiaryAnalysis() {
        return "redirect:http://localhost:5000/file";
    }

    @GetMapping("/redirectToHobbyBoard")
    public String redirectToHobbyBoard() {
        return "redirect:http://localhost:8080/question/list";
    }

    @GetMapping("/myInfo")
    public String myInfo() {
        return "myInfo";
    }


}