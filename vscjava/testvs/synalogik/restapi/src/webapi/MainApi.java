package vscjava.testvs.synalogik.restapi.src.webapi;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/mainApi/")
public class MainApi {
    
    @GetMapping("/health")
    public String isOnline()
    {
        return "Main Api OK!";
    }

}
