package com.cums.image;

import java.util.Base64;
import java.util.List;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AlbumController {

    @Autowired
    private AlbumImagesRepository imageRepository;

    @GetMapping("/album")
    public String album(Model model) {
        List<AlbumImages> images = imageRepository.findAll();

        // 이미지 데이터를 Base64로 인코딩하여 문자열 리스트로 변환
        List<String> imagePaths = images.stream()
            .map(image -> "data:image/png;base64," + Base64.getEncoder().encodeToString(image.getData()))
            .collect(Collectors.toList());

        // 이미지 데이터 리스트를 모델에 추가하여 Thymeleaf로 전달
        model.addAttribute("imagePaths", imagePaths);
        model.addAttribute("images", images);
        // 앨범 페이지로 이동
        return "album";
    }
}
